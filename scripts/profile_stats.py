#!/usr/bin/env python3
"""Generate self-hosted GitHub stats cards for the profile README.

Runs in GitHub Actions with the built-in GITHUB_TOKEN (public data only) and
writes assets/github-stats.svg and assets/top-langs.svg. Standard library only.

Usage:
  profile_stats.py                  # fetch live data (needs GITHUB_TOKEN)
  profile_stats.py --placeholder    # write "refresh pending" cards
  profile_stats.py --fixture F.json # render from a saved API response (tests)
"""
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from xml.sax.saxutils import escape

LOGIN = os.environ.get("PROFILE_LOGIN", "creator35lwb-web")
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")

# "radical" palette, matching the rest of the profile
BG, BORDER, TITLE, TEXT, ICON = "#141321", "#e4e2e2", "#fe428e", "#a9fef7", "#f8d847"
FONT = "'Segoe UI', Ubuntu, 'Helvetica Neue', Sans-Serif"

QUERY = """
query($login: String!, $after: String) {
  user(login: $login) {
    name
    followers { totalCount }
    pullRequests { totalCount }
    issues { totalCount }
    contributionsCollection {
      totalCommitContributions
      restrictedContributionsCount
    }
    repositories(first: 100, after: $after, ownerAffiliations: OWNER,
                 privacy: PUBLIC, isFork: false) {
      totalCount
      pageInfo { hasNextPage endCursor }
      nodes {
        stargazerCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
  }
}
"""


def graphql(token, variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {token}", "User-Agent": "profile-stats"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.load(resp)
    if payload.get("errors"):
        raise RuntimeError(payload["errors"])
    return payload["data"]["user"]


def fetch(token):
    user, repos, after = None, [], None
    while True:
        page = graphql(token, {"login": LOGIN, "after": after})
        user = user or page
        repos.extend(page["repositories"]["nodes"])
        info = page["repositories"]["pageInfo"]
        if not info["hasNextPage"]:
            break
        after = info["endCursor"]
    user["repositories"]["nodes"] = repos
    return user


def summarize(user):
    repos = user["repositories"]["nodes"]
    langs = {}
    for repo in repos:
        for edge in repo["languages"]["edges"]:
            name = edge["node"]["name"]
            size, color = langs.get(name, (0, edge["node"]["color"]))
            langs[name] = (size + edge["size"], color or "#858585")
    cc = user["contributionsCollection"]
    return {
        "name": user.get("name") or LOGIN,
        "stars": sum(r["stargazerCount"] for r in repos),
        "repos": user["repositories"]["totalCount"],
        "commits": cc["totalCommitContributions"] + cc["restrictedContributionsCount"],
        "prs": user["pullRequests"]["totalCount"],
        "issues": user["issues"]["totalCount"],
        "followers": user["followers"]["totalCount"],
        "langs": sorted(langs.items(), key=lambda kv: kv[1][0], reverse=True)[:8],
    }


def card(width, height, title, body, footer):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}">
  <title>{escape(title)}</title>
  <rect x="0.5" y="0.5" rx="4.5" width="{width - 1}" height="{height - 1}" fill="{BG}" stroke="{BORDER}" stroke-opacity="0.2"/>
  <text x="25" y="35" fill="{TITLE}" font-family="{FONT}" font-size="18" font-weight="600">{escape(title)}</text>
{body}
  <text x="{width - 20}" y="{height - 12}" text-anchor="end" fill="{TEXT}" fill-opacity="0.55" font-family="{FONT}" font-size="10">{escape(footer)}</text>
</svg>
"""


def stats_svg(s, footer):
    rows = [
        ("Total stars earned", s["stars"]),
        ("Public repositories", s["repos"]),
        ("Commits (last 12 months)", s["commits"]),
        ("Pull requests", s["prs"]),
        ("Issues", s["issues"]),
        ("Followers", s["followers"]),
    ]
    body = "\n".join(
        f'  <circle cx="31" cy="{66 + i * 25}" r="4" fill="{ICON}"/>'
        f'<text x="45" y="{70 + i * 25}" fill="{TEXT}" font-family="{FONT}" font-size="14" font-weight="600">{escape(label)}:</text>'
        f'<text x="300" y="{70 + i * 25}" fill="{TEXT}" font-family="{FONT}" font-size="14" font-weight="700">{value:,}</text>'
        for i, (label, value) in enumerate(rows)
    )
    return card(420, 230, f"{s['name']}'s GitHub Stats", body, footer)


def langs_svg(langs, footer):
    total = sum(size for _, (size, _) in langs) or 1
    bar, x = [], 25.0
    for name, (size, color) in langs:
        w = 250 * size / total
        bar.append(f'<rect x="{x:.2f}" y="55" width="{w:.2f}" height="8" fill="{color}"/>')
        x += w
    items = []
    for i, (name, (size, color)) in enumerate(langs):
        cx, cy = 25 + (i % 2) * 130, 88 + (i // 2) * 22
        items.append(
            f'<circle cx="{cx + 5}" cy="{cy - 4}" r="5" fill="{color}"/>'
            f'<text x="{cx + 15}" y="{cy}" fill="{TEXT}" font-family="{FONT}" font-size="11">{escape(name)} {100 * size / total:.1f}%</text>'
        )
    height = 105 + ((len(langs) + 1) // 2) * 22
    body = "  <clipPath id=\"bar\"><rect x=\"25\" y=\"55\" width=\"250\" height=\"8\" rx=\"4\"/></clipPath>\n"
    body += f'  <g clip-path="url(#bar)">{"".join(bar)}</g>\n  ' + "\n  ".join(items)
    return card(300, max(height, 150), "Most Used Languages", body, footer)


def placeholder():
    body = f'  <text x="25" y="75" fill="{TEXT}" font-family="{FONT}" font-size="14">Stats refresh pending: generated daily by GitHub Actions.</text>'
    return card(420, 120, "GitHub Stats", body, ""), card(300, 120, "Most Used Languages", body.replace("420", "300"), "")


def write(name, content):
    with open(os.path.join(OUT_DIR, name), "w", encoding="utf-8") as fh:
        fh.write(content)


def main(argv):
    if "--placeholder" in argv:
        stats, langs = placeholder()
    else:
        if "--fixture" in argv:
            with open(argv[argv.index("--fixture") + 1], encoding="utf-8") as fh:
                user = json.load(fh)
        else:
            token = os.environ.get("GITHUB_TOKEN")
            if not token:
                sys.exit("GITHUB_TOKEN is required")
            user = fetch(token)
        s = summarize(user)
        footer = "Updated " + datetime.now(timezone.utc).strftime("%Y-%m-%d") + " UTC"
        stats, langs = stats_svg(s, footer), langs_svg(s["langs"], footer)
    write("github-stats.svg", stats)
    write("top-langs.svg", langs)


if __name__ == "__main__":
    main(sys.argv[1:])

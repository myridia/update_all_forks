#! env/bin/python
import sys
import requests
import json
import os
from github import Github
from charset_normalizer import md__mypyc


def main(token):
    g = Github(token)

    g_user = g.get_user()

    # put here your list you like to ignore
    ignore_repos = ["amazon-e-commerce-clone-app", "cli-media-cleanup"]

    amount = 0
    count = 0
    # Loop the projects

    for repo in g_user.get_repos():
        amount += 1
        # print(repo.name,repo.fork, repo.parent, repo.source)
        if repo.fork:
            repo_parent_commit = repo.parent.get_branch(
                repo.parent.default_branch
            ).commit.sha
            repo_commit = repo.get_branch(repo.default_branch).commit.sha
            print(repo.name)
            print("parent comit:", repo_parent_commit)
            print("repro commit:", repo_commit)

            if (not repo_commit == repo_parent_commit) and (
                repo.name not in ignore_repos
            ):
                print(
                    "...different {0} ==> {1}".format(
                        repo.full_name, repo.parent.full_name
                    )
                )
                print("...fork branch: {0}".format(repo.default_branch))
                # https://dev.to/n3wt0n/3-ways-to-sync-a-forked-repository-on-github-automatically-cfd
                url = "https://api.github.com/repos/{0}/merge-upstream".format(
                    repo.full_name
                )
                headers = {
                    "user-agent": "my-app/0.0.1",
                    "Accept": "application/vnd.github.v3+json",
                    "Authorization": "token {}".format(token),
                }
                data = {"branch": repo.default_branch}
                resp = requests.post(url=url, data=json.dumps(data), headers=headers)
                print(resp.content)
                # print(url)
                # print(headers)
                # print(data)

            # else:
            # print('...failed')
            #    pass


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1].startswith("--token="):
            a = sys.argv[1].split("=")
            token = a[1]
            main(token)
    else:
        print("...missing token")
        print("...example of usage:")
        print("./main.py --token=ghp_2GcjnhBdwa9v4aoB4ABC123xsxDRBL84JaZDA")

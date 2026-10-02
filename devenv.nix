{ pkgs, ... }:
{
  name = "2026-DExB2";

  languages.python = {
    enable = true;
    version = "3.12";
    venv.enable = true;
    uv = {
      enable = true;
      sync.enable = true;
    };
  };

  packages = [
    pkgs.git
    pkgs.zlib
    pkgs.stdenv.cc.cc.lib
  ];

  scripts.lab.exec = ''
    exec jupyter lab "$@"
  '';

  scripts.sync.exec = ''
    set -euo pipefail

    for arg in "$@"; do
      case "$arg" in
        -h|--help)
          echo "usage: sync"
          echo
          echo "  Fast-forwards main to upstream/main, then merges main into the"
          echo "  branch you started on."
          exit 0
          ;;
        *) echo "sync: unknown argument '$arg' (try --help)" >&2; exit 2 ;;
      esac
    done

    cd "$DEVENV_ROOT"

    if ! git diff --quiet HEAD; then
      echo "✗ You have uncommitted changes. Commit or stash them first." >&2
      exit 1
    fi

    branch=$(git rev-parse --abbrev-ref HEAD)

    echo "• Fetching upstream (the course repo)..."
    git fetch upstream

    echo "• Fast-forwarding main to upstream/main..."
    git checkout --quiet main
    if ! git merge --ff-only upstream/main; then
      echo "✗ Your main has commits of its own, so it cannot fast-forward." >&2
      echo "  Keep main a pure mirror of upstream; put your work on a branch." >&2
      git checkout --quiet "$branch"
      exit 1
    fi

    if [ "$branch" != "main" ]; then
      echo "• Merging main into $branch..."
      git checkout --quiet "$branch"
      git merge --no-edit main
    fi

    echo "✓ $branch is up to date with upstream."
  '';
  
  tasks."dexb2:python-test" = {
    after = [ "devenv:enterShell" ];
    before = [ "devenv:enterTest" ];
    exec = ''
      python -c 'import numpy, pandas, scipy, seaborn, matplotlib, openpyxl, xlrd'
      jupyter --version
    '';
  };
}

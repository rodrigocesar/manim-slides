# shellcheck shell=bash
# Shared helpers. Source from other scripts after ROOT is set.

talks_dir() {
  echo "${ROOT}/presentations"
}

list_talks() {
  find "$(talks_dir)" -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | sort
}

resolve_talk() {
  local name="${1:-}"
  if [[ -z "${name}" ]]; then
    echo "Usage: $0 <talk> [...]" >&2
    echo "Talks:" >&2
    list_talks | sed 's/^/  /' >&2
    exit 1
  fi
  local dir
  dir="$(talks_dir)/${name}"
  if [[ ! -d "${dir}" ]]; then
    echo "Unknown talk: ${name}" >&2
    echo "Talks:" >&2
    list_talks | sed 's/^/  /' >&2
    exit 1
  fi
  if [[ ! -f "${dir}/talk.json" ]]; then
    echo "Missing ${dir}/talk.json" >&2
    exit 1
  fi
  echo "${dir}"
}

talk_title() {
  python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["title"])' "$1/talk.json"
}

talk_scenes() {
  python3 -c 'import json,sys; print("\n".join(json.load(open(sys.argv[1]))["scenes"]))' "$1/talk.json"
}

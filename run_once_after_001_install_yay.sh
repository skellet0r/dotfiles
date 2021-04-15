#!/bin/bash

TEMP_DIR=$(mktemp -d)
GIT_URL=https://aur.archlinux.org/yay.git

if ! command -v git 1>/dev/null 2>&1; then
  echo "yay: Git is not installed, can't continue." >&2
  exit 1
fi

failed_checkout() {
  echo "Failed to git clone $1"
  exit -1
}

checkout() {
  [ -d "$2" ] || git clone --depth 1 "$1" "$2" || failed_checkout "$1"
}

checkout "${GIT_URL}" "${TEMP_DIR}/yay"
pushd "${TEMP_DIR}/yay"
makepkg -si

popd

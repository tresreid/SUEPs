install_env() {
  set -e
  echo "Installing shallow virtual environment in $PWD/.env..."
  python -m venv --without-pip --system-site-packages .env
  unlink .env/lib64  # HTCondor can't transfer symlink to directory and it appears optional
  # work around issues copying CVMFS xattr when copying to tmpdir
  export TMPDIR=$(mktemp -d -p .)
  .env/bin/python -m ipykernel install --user
  rm -rf $TMPDIR && unset TMPDIR
  .env/bin/python -m pip install -q git+https://github.com/CoffeaTeam/lpcjobqueue.git@v0.2.5
  echo "done."
}

export JUPYTER_PATH=/srv/.jupyter
export JUPYTER_RUNTIME_DIR=/srv/.local/share/jupyter/runtime
export JUPYTER_DATA_DIR=/srv/.local/share/jupyter
export IPYTHONDIR=/srv/.ipython

[[ -d .env ]] || install_env
source .env/bin/activate
alias pip="python -m pip"

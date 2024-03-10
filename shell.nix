let
  pinned =
    import (builtins.fetchTarball {
      name = "nixos-23.05";
      url = https://github.com/NixOS/nixpkgs/archive/refs/tags/23.05.tar.gz;
      sha256 = "10wn0l08j9lgqcw8177nh2ljrnxdrpri7bp0g7nvrsn9rkawvlbf";
    }){};

  poetry_py311 = pinned.poetry.override {
    python3 = pinned.python311;
  };

in
  with pinned;

  mkShell {
    # Dependencies.
    nativeBuildInputs = with pkgs.buildPackages; [
      poetry
      postgresql_14
      pre-commit
      python311
      python311Packages.pip
      python311Packages.setuptools
      readline
      sentry-cli
      sqlite
      stdenv.cc.cc.lib
      terraform
      tflint
      xz
      zlib
    ];
}

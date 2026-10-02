{ pkgs, ... }:
{
  name = "my-rosalind";

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

  tasks."myrl:python-test" = {
    after = [ "devenv:enterShell" ];
    before = [ "devenv:enterTest" ];
    exec = ''
      python -c 'import numpy, pandas, scipy, seaborn, matplotlib, openpyxl, xlrd'
      jupyter --version
    '';
  };
}

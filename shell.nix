{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    python3Packages.numpy
    python3Packages.pillow
    python3Packages.flask
    python3Packages.requests
    basedpyright
  ];
}

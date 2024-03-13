
{
  description = "A flake for the LPM discretization library.";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {self, nixpkgs, flake-utils, ... }: flake-utils.lib.eachDefaultSystem (system:
    let
      pkgs = import nixpkgs {
        inherit system;
      };
      discretization = pkgs.python310Packages.buildPythonPackage {
        pname = "lpm_discretize";
        version = "0.0.1";
        src = self;
        nativeBuildInputs = with pkgs.python310Packages; [
          setuptools
        ];
        nativeCheckInputs = with pkgs.python310Packages; [
          pytest
          numpy
          polars
        ];
        checkPhase = "pytest tests/ -vvv";
        propagatedBuildInputs = (with pkgs.python310Packages; [
          numpy
          polars
        ]);
      };
    in rec
      {
        devShells.default = pkgs.mkShell {
          buildInputs = [
          discretization
          pkgs.python310Packages.pytest # Adding pytest here so that developers can run the tests.
          ];
        };
        packages.default = discretization;
        apps.default = {
          type = "app";
          program = "${discretization}/bin/discretize";
        };
      }
  );
}

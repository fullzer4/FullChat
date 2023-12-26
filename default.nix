{ lib, buildRustPackage, fetchFromGitHub }:

buildRustPackage rec {
  pname = "notesynk";
  version = "0.1.0";

  src = fetchFromGitHub {
    owner = "fullzer4";
    repo = "NoteSynk";
    rev = "v${version}";
    sha256 = "...";
  };

  cargoSha256 = "...";

  meta = with lib; {
    description = "Descrição do meu projeto";
    license = licenses.mit;
  };
}

import { parse } from "https://deno.land/std@0.200.0/flags/mod.ts";
import type { Args } from "https://deno.land/std@0.200.0/flags/mod.ts";

const parseArguments = (args: string[]): Args => {

  const booleanArgs = [
    "help",
    "save",
  ]

  const stringArgs = [
    "folder",
    "timeout",
  ];

  const alias = {
    "help": "h",
    "save": "s",
    "folder": "f",
    "timeout": "t",
  };

  return parse(args, {
    alias,
    boolean: booleanArgs,
    string: stringArgs,
    stopEarly: false,
    "--": true,
  });
}

export default parseArguments

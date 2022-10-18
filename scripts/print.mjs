#!/usr/bin/env zx

const commands = process.argv.slice(4, process.argv.length);

echo(commands.join("\n"));

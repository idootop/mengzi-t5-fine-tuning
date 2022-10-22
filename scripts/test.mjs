#!/usr/bin/env zx

const command = process.argv[3] ?? "index";
const commands = process.argv.slice(4, process.argv.length);

await $`python ./tests/${command}_test.py ${commands}`;

// news-image-20261126 — entrypoint (Node 22, standard library only).
//
// The entry is a single image, entry.png, drawn for Thursday 26 November 2026:
// a newspaper front page summing up the day's world news (US tariffs on 14
// trading partners, the Kyiv strikes, the Kuwait drone attack, the new ECB
// chief, the tanker capsized off Ibiza, plus Ebola, the HIV jab and
// Thanksgiving in the footer). This program copies that image to the output
// directory so the judge sees exactly its bytes.
//
// Run locally with:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
// In the grader MAKEFUN_OUTPUT_DIR is /output. No network, no arguments.
// The copy is byte-for-byte, so repeated runs write identical output.

import { copyFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const repoDir = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(join(repoDir, 'entry.png'), join(outDir, 'entry.png'));

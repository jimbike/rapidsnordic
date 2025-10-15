import { defineConfig } from 'astro/config';
export default defineConfig({
  site: 'https://example.com',
  srcDir: './src',
  server: { port: 4321 },
});

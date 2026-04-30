import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  base: './',
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        'index-en': resolve(__dirname, 'index-en.html'),
        proyectos: resolve(__dirname, 'proyectos.html'),
        'proyectos-en': resolve(__dirname, 'proyectos-en.html'),
        diseno: resolve(__dirname, 'diseno.html'),
        'diseno-en': resolve(__dirname, 'diseno-en.html'),
        'ux-ui': resolve(__dirname, 'ux-ui.html'),
        'ux-ui-en': resolve(__dirname, 'ux-ui-en.html'),
        'cv-impresion': resolve(__dirname, 'cv-impresion.html'),
        'cv-impresion-en': resolve(__dirname, 'cv-impresion-en.html'),
      },
    },
  },
});

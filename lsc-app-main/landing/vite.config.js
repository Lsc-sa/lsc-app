import path from 'path';
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
// import proxyOptions from './proxyOptions';

// https://vitejs.dev/config/
export default defineConfig({
	plugins: [vue()],
	// server: {
	// 	port: 8080,
	// 	proxy: proxyOptions
	// },
	resolve: {
		alias: {
			'@': path.resolve(__dirname, 'src')
		}
	},
	build: {
		outDir: '../lsc_api/public/landing',
		emptyOutDir: true,
		target: 'es2015',
	},
});

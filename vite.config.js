import { defineConfig } from 'vite';
import dotenv from 'dotenv';

dotenv.config();

export default defineConfig({
    define: {
        'process.env': {
            VITE_API_KEY: process.env.VITE_API_KEY,
            VITE_AUTH_DOMAIN: process.env.VITE_AUTH_DOMAIN,
            VITE_PROJECT_ID: process.env.VITE_PROJECT_ID,
            VITE_STORAGE_BUCKET: process.env.VITE_STORAGE_BUCKET,
            VITE_MESSAGING_SENDER_ID: process.env.VITE_MESSAGING_SENDER_ID,
            VITE_APP_ID: process.env.VITE_APP_ID,
        }
    }
});

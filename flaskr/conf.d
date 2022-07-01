server {
    listen 80;
    server_name 3.34.252.254;
    charset utf-8;

    error_log /var/log/nginx/error.log;

    location / {
        proxy_pass http://web:5000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
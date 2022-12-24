# Product CRUD

Clone source code aplikasi\
`git clone https://github.com/arrazy100/productCRUD.git`\
\
Berpindah ke folder source code\
`cd productCRUD`

## Menjalankan program dengan docker-compose

Masukkan perintah di bawah ini ke terminal jika menjalankan pertama kali\
`sudo docker-compose up --build`\
\
Masukkan perintah di bawah ini jika sudah pernah menjalankan aplikasi\
`sudo docker-compose up`

## Menjalankan program tanpa docker-compose

Build image untuk Django web\
`docker build -t web_product_crud ./ProductCRUD`\
\
Build image untuk nginx\
`docker build -t nginx_product_crud ./nginx`\
\
Membuat network untuk menghubungkan django, postgresql, dan nginx\
`docker network create app_net`\
\
Run docker container postgresql\
`docker run --env-file ./.env.dev -v postgres_data:/var/lib/postgresql/data/ --net=app_net --name db postgres:13.0`\
\
Run docker container untuk web Django\
`docker run -v static_volume:/usr/src/productCRUD/staticfiles/ --expose 8000 --env-file ./.env.dev --restart always --network app_net --link db:db --name web web_product_crud /bin/sh -c /usr/src/productCRUD/django-entrypoint.sh`\
\
Run docker container untuk nginx\
`docker run -v static_volume:/usr/src/productCRUD/staticfiles/ -p 8000:8000 --network app_net --link web:web --name nginx nginx_product_crud`

## Menghentikan program dengan docker-compose\
\
Jalankan perintah di bawah  ini untuk menghentikan program\
`sudo docker-compose stop`\
\
Jalankan perintah di bawah ini untuk menghapus container\
`sudo docker-compose down -v`

## Menghentikan program tanpa docker-compose

Jalankan perintah di bawah untuk menghentikan semua container\
`docker stop db web nginx`\
\
Untuk menjalankan program kembali masukkan perintah berikut\
`docker start db web nginx`\
\
Jalankan perintah di bawah untuk menghapus container\
`docker rm db web nginx`

## Membuka website Product CRUD

Buka browser dan masukkan url berikut [http://localhost:8000](http://localhost:8000)
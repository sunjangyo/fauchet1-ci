SRC="/media/jin/4abb279b-6d65-4663-97c2-26987f64673a/home/yuna/Tools"

nohup $SRC/cloudflared tunnel --no-autoupdate --url "http://127.0.0.1:80" > /tmp/ltunnel.log 2>&1 &
sleep 10
URL=$(grep -o 'https://[a-z0-9-]*\.trycloudflare\.com' /tmp/ltunnel.log | head -1)

if [ -n "$URL" ]; then
    echo "[+] URL: $URL"
else
    echo "[!] Failed tunnel: $URL"
    exit
fi

gh workflow run build.yml --ref main -f mode=boot -f loop=true -f argumen="$URL"




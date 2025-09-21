## Django, Nginx, Docker-compose
Django, Nginx, Docker-comose를 사용하여 배포하는 방법.
기본적으로 public repository로 유지하고 서버에서 pull 받아서 docker-compose up -d 로 서버를 한 번에 구성한다.

## Development
ec2 서버 superuser 비밀번호 세팅
```
sudo passwd root
```
설정 이후 루트 계정으로 쭉 운영하기 위해 슈퍼유저로 로그인
```
su -
```

Linux 환경 업그레이드
```
apt update

```

Docker 환경을 위해 패키지 설치
```
apt install apt-transport-https 
apt install ca-certificates
apt install curl
apt install software-properties-common
```

Curl 명령어로 Docker 다운로드
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add
```

Repository에 경로 추가
```
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt-get update
```

Docker Engine 설치
```
apt-get install docker-ce docker-ce-cli containerd.io
```

Docker Compose 설치 (최신 버전으로 바꾸려면 버전 명만 변경)
```
curl -L "https://github.com/docker/compose/releases/download/2.5.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

권한 부여
```
chmod +x /usr/local/bin/docker-compose
```

설치 여부 확인
```
docker -v
docker-compose -v
```

.env.example 파일 바탕으로 .env 파일 생성 및 vi로 수정
```
cp .env.example .env
vi .env
```
---

## Docker 관련 명령어

실행 중인 Docker 컨테이너 리스트 (-qa 제외하면 모든 컨테이너 리스트)
```
docker ps -qa
```

Docker 컨테이너 모두 삭제
```
docker rm -f $(docker ps -qa)
```

Docker 이미지 리스트
```
docker image ls -a
```

Docker 이미지 모두 삭제
```
docker rmi $(docker images -q)
```

Pull 이상 있을 시
```
git fetch --all
git reset --hard origin/main 아니면 origin/master 등등
```

---

## HTTPS 적용 가이드

본 리포는 다음과 같이 HTTPS를 지원하도록 구성되어 있습니다.

- docker-compose: Nginx 443 포트 노출(ports: 443:443) 및 인증서 경로 마운트(./nginx/certs → /etc/nginx/certs).
- Nginx: 80 → 443 리다이렉트, 443에서 TLS 종료 후 Django로 프록시, X-Forwarded-Proto 헤더 전달.
- Django(settings.py): SECURE_PROXY_SSL_HEADER, USE_X_FORWARDED_HOST, (DEBUG=False 시) SECURE_SSL_REDIRECT/HSTS/보안 쿠키, CSRF_TRUSTED_ORIGINS 환경변수 지원.

필수 준비물
- 도메인과 인증서 파일(실서버: 발급된 fullchain.pem, privkey.pem / 테스트: self-signed 가능).
- 인증서 파일 위치: 프로젝트 ./nginx/certs/fullchain.pem, ./nginx/certs/privkey.pem

배포/실행 요약
1) 인증서 파일을 위 경로에 배치한다.
2) 환경변수(.env)에 운영 시 다음을 설정한다.
   - DEBUG=False
   - CSRF_TRUSTED_ORIGINS=https://example.com,https://www.example.com (필요 도메인 나열)
   - (옵션) SECURE_SSL_REDIRECT=True, SECURE_HSTS_SECONDS=31536000
3) DNS를 서버 공인 IP로 설정한다.
4) 컨테이너 재시작 후 http로 접속 시 https로 리다이렉트된다.

참고: Let’s Encrypt 사용 시
- webroot(/.well-known/acme-challenge) 경로가 Nginx에 열려 있으므로 certbot(webroot 모드)로 인증서를 발급 후 ./nginx/certs에 배치하면 된다.
- 인증서 갱신 시 컨테이너를 재시작하여 Nginx가 새 인증서를 읽도록 한다.

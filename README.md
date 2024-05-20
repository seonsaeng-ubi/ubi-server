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

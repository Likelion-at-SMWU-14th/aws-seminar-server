# AWS Seminar Server

멋쟁이사자처럼 숙명여대 14기 백엔드 AWS 배포 세미나용 Django 서버입니다.

EC2 인스턴스에서 Django 프로젝트를 실행하고, 퍼블릭 IP를 통해 서버 응답을 확인하는 실습을 위한 레포지토리입니다.

## 주요 기능

- Django 서버 실행 확인
- 기본 텍스트 응답 확인
- JSON 응답 확인
- EC2 퍼블릭 IP를 통한 외부 접속 확인
- Postman을 이용한 API 응답 확인

## API

| Method | URL | Description |
| --- | --- | --- |
| GET | `/` | 기본 서버 응답 확인 |
| GET | `/health/` | 서버 상태 확인용 JSON 응답 |
| GET | `/api/` | API 명세서 작성용 샘플 JSON 응답 |

## 응답 예시

### GET `/`

```text
Hello, AWS!

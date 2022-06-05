# git 관련
# Untracked files:  추적되지 않은파일
# Head 현재위치

# git init  .git 하위 디렉토리 생성
# 폴더를 만든후 그안에서 명령실행 -> 새로운 git 저장소 생성
# git lg 정리해주는거 (이쁘게)
# git status (현재상태 바뀐거랑 새파일 나옴)
# git remote 현 폴더의 레파지토리를 확인하는 명령어
# git remote -v 연결고리확인

# git branch 모든 branch 가 나옴 ( 현재 brancg가 나옴)
# git checkout (branch 이름) 쓰면 그 brancg Head로 이동
# git checkout -b (branch 이름) 브랜치 생성 이동
# git branch -d (branch 이름) 브랜치 삭제

# 1 add
# git add test.py / git add -A (전부)

# 2 commit
# git commit -m " 메 세 지 "

# 3 push
# git push -> 첫번째 푸시는 git push --set-upstream origin master

# git checkout (해시주소를 입력) -> 그때의 상태로감
# git log -> 주소가 나옴(고유번호, 중복x 주소개념)
# commit 마다 고유한 해시가 있다
# git log 치고 못빠져나올때 (q + 콜론 누르면 나오게됨)

# git merge <다른 Branch 이름> 현재브랜치에 다른 브랜치의
# 수정사항 병합 (merge 후에도 push 해야함)

# 파일 움직일때 cd 파일명
# git 움직일때 git checkout commit명 or branch명 그위치로감

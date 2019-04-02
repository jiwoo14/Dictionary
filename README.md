# Dictionary
likelion
# 오류내용 + 해결방법
1. 가변 인자 사용 - 

# 간단한 소감

# 참고문서
1. datetime 모듈 : https://datascienceschool.net/view-notebook/465066ac92ef4da3b0aba32f76d9750a/
2. 유용한 python 모듈 : http://w3devlabs.net/wp/?p=16873
3. 가변 인자 사용법 : https://mingrammer.com/understanding-the-asterisk-of-python/
# 기록
1. python에는 positional arguments와 keyword arguments라는 두 가지 종류의 인자가 있다. 전자의 경우 생략이 불가능하며 갯수대로 정해진 위치에 인자를 전달해야 한다. 반면 후자의 경우, 함수 선언 시 디폴트 값을 설정할 수 있으며, 만약 인자를 생략할 시 해당 디폴트 값이 인자의 값으로 들어간다. 즉, 이 형태의 인자는 생략이 가능하다. 후자의 경우 생략이 가능하기 때문에, 전자 이전에 선언될 수 없다.
2. keyword argument는 (name)=None의 형식으로 선언한다.
3. 가변인자(Variadic Arguments)는 positional arguments와 keyword arguments에 모두 사용할 수 있다. 전자의 경우 *args, 후자의 경우 **kwargs를 사용한다. >> 이런 형태로 가변인자를 받는 것을 packing이라고 한다.

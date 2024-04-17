class manage:
    def __init__(self):
        self.number = []        # 학번 배열
        self.name = []          # 이름 배열
        self.eng = []           # 영어 성적 배열
        self.c = []             # C언어 성적 배열
        self.py = []            # 파이썬 성적 배열
        self.total = []         # 총점 배열
        self.average = []       # 평균 배열
        self.grade = []         # 학점 배열
        self.rank = []          # 등수 배열
        self.check = []         # 등수 만드는 용도
        self.student_num = 0    # 입력받은 학생 수
        self.count = 0          # 80점 이상 학생 수

    def input_info(self):       # 정보 입력 함수
        self.number.append(input("학번: "))
        self.name.append(input("이름: "))
        self.eng.append(int(input("영어: ")))
        self.c.append(int(input("C-언어: ")))
        self.py.append(int(input("파이썬: ")))
        self.student_num += 1

    def tot_ave(self, student_num):  # 총점, 평균 계산용 함수
        total = self.eng[student_num] + self.c[student_num] + self.py[student_num]
        average = total / 3
        self.total.append(total)
        self.average.append(average)
        self.check.append(average)
        if average >= 80:
            self.count += 1

    def abc(self, student_num):     # 학점 판정 함수
        if self.average[student_num] >= 95:
            self.grade.append('A+')
        elif self.average[student_num] >= 90:
            self.grade.append('A0')
        elif self.average[student_num] >= 85:
            self.grade.append('B+')
        elif self.average[student_num] >= 80:
            self.grade.append('B0')
        elif self.average[student_num] >= 75:
            self.grade.append('C+')
        elif self.average[student_num] >= 70:
            self.grade.append('C0')
        else:
            self.grade.append('F')

    def ranking(self):      # 등수 판정 함수(출력하기 직전에 사용)
        for i in range(self.student_num):
            minimum = self.check[i]
            min_index = i
            for k in range(i, self.student_num):
                if self.check[k] < minimum:
                    minimum = self.check[k]
                    min_index = k
            temp = self.check[i]
            self.check[i] = minimum
            self.check[min_index] = temp
        for i in range(self.student_num):
            for k in range(self.student_num):
                if self.average[i] == self.check[k]:
                    self.rank.append(i + 1)
                    break

    def delete_info(self, index):       # 정보 삭제 함수
        if self.average[index] >= 80:
            self.count -= 1
        del self.name[index]
        del self.number[index]
        del self.eng[index]
        del self.c[index]
        del self.py[index]
        del self.total[index]
        del self.average[index]
        del self.grade[index]
        del self.check[index]
        self.student_num -= 1

    def output_info(self):      # 정보 출력 함수
        print("\t\t성적관리 프로그램")
        print("===============================================================================")
        print("\t학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
        print("===============================================================================")
        for i in range(self.student_num):
            print(f"{self.number[i]:<10}\t{self.name[i]}\t{self.eng[i]}\t{self.c[i]}\t{self.py[i]}\t{self.total[i]}\t{self.average[i]}\t{self.grade[i]}\t{self.rank[i]}")
        print("평균 80점 이상 학생 수:", self.count)

    def run(self):      # 성적 관리 프로그램 실행
        while True:
            print("=============menu==================")
            print("1.입력")
            print("2.삭제")
            print("3.출력")
            print("===================================")
            menu = int(input("번호를 입력하세요 1~3 : "))   # 메뉴 항목 입력

            if menu == 1:   # 입력
                self.input_info()
                self.tot_ave(self.student_num - 1)
                self.abc(self.student_num - 1)

            elif menu == 2: # 삭제
                if self.student_num < 1:
                    print("삭제할 정보가 없습니다.")
                else:
                    what = int(input("삭제할 성적의 정보(번호)를 고르세요.(1.이름, 2. 학번): "))
                    if what == 1:
                        w_name = input("이름을 입력하세요: ")
                        index = self.name.index(w_name)
                        self.delete_info(index)
                    elif what == 2:
                        w_num = input("학번을 입력하세요: ")
                        index = self.number.index(w_num)
                        self.delete_info(index)
                    else:
                        print("잘못된 입력입니다.")

            elif menu == 3: # 출력
                if self.student_num < 1:
                    print("출력할 정보가 없습니다.")
                else:
                    self.ranking()
                    self.output_info()
                    break
            else:
                print("잘못된 입력입니다.")

manager = manage()      # 프로그램 실행
manager.run()

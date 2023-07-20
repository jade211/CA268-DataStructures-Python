# QUESTION 1 -> Worked on by Jade Hudson and Sruthi Santhosh


def q1_sum(lst):
   total = 0
   for x in lst:
      for num in x:
          if int(num) % 2 == 0:
             total = total + int(num)
          else:
            total = total
   return total

lst = [[1, 0, 2], [5, 5, 7], [9, 4, 3]]
print(q1_sum(lst))




# QUESTION 2 -> Worked on by Jade Hudson and Sruthi Santhosh


def move_vow(sentence):
   v = "aeiouAEIOU"
   vowels = []
   cons = []
   for s in sentence:
      if s in v:
         vowels.append(s)
      else:
         cons.append(s)
   result = ''.join(vowels) + ''.join(cons)
   return result


print(move_vow('This is DCU!'))




# QUESTION 3 -> Worked on by Jade Hudson and Sruthi Santhosh


def greetings(name):
    guests = {
    'Randy': 'Germany',
    'Karla': 'France',
    'Wendy': 'Japan',
    'Norman': 'England',
    'Sam': 'Argentina'
    }

    if name in guests:
       country = guests[name]
    else:
       country = ""
    if len(country) > 0:
       return f"Hi! I'm {name} and I'm from {country}."
    else:
       return f"Hi! I'm {name}"


print(greetings("Sam"))




# QUESTION 4 -> Worked on by Jade Hudson and Sruthi Santhosh


class Memories(object):
    def __init__(self, name, age, salary):
      self.name = name
      self.age = age
      self.salary = salary
      self.d = {}

    def remember(self, x):
        self.d["name"] = self.name
        self.d["age"] = self.age
        self.d["salary"] = self.salary
        if x in self.d:
            return self.d[x]
        else:
            return False


person1 = Memories(name='Tom', age=32, salary=50000)
print(person1.remember('salary'))
print(person1.remember('email'))




# QUESTION 5


class Test(object):
    def __init__(self, subject_name, correct_answers, passing_mark):
        self.subject_name = subject_name
        self.correct_answers = correct_answers
        self.passing_mark = passing_mark


class Student(object):
    def __init__(self, name):
        self.name = name

    def take_test(self, paper, student_answers):
        total = 0
        i = 0
        while i < len(paper.correct_answers):
            if paper.correct_answers[i] == student_answers[i]:
                total = total + 1
            i = i + 1
        if (total / len(paper.correct_answers) * 100) >= int(paper.passing_mark[: -1]):
            return(f"{self.name} passed the {paper.subject_name} test with the score {(total / len(paper.correct_answers)) * 100}%")
        else:
            return(f"{self.name} failed the {paper.subject_name} test!")


paper1 = Test('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
paper2 = Test('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
paper3 = Test('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

stu1 = Student('Tom')
print(stu1.take_test(paper2, ['1C', '2C', '3D', '4A']))

stu2 = Student('John')
print(stu2.take_test(paper1, ['1B', '2C', '3A', '4A', '5B']))




# QUESTION 6


def histogram(nums, char):
    result = []
    for num in nums:
        result.append(char * num)
    return"\n".join(result)


print(histogram([6, 2, 15 , 3, 20 , 5], '=' ))




# QUESTION 7


def filter_star(d, num):
    result_d = {}
    for k, v in d.items():
        if len(v) == num:
            result_d[k] = v
    if len(result_d) > 0:
        return result_d
    else:
        return "No result found!"


print(filter_star({
  'Luxury Chocolates': '*****',
  'Tasty Chocolates': '****',
  'Big Chocolates': '*****',
  'Generic Chocolates': '***'
}, 5))

print(filter_star({
  'Luxury Chocolates': '*****',
  'Tasty Chocolates': '****',
  'Big Chocolates': '*****',
  'Generic Chocolates': '***'
}, 2))

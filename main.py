from search import Search, print_result
from initialize import init


def auto_complete():
    print("Loading the files and preparing the system...")
    init()
    print("The system is ready. Enter your text:")
    user_input = ""
    while True:
        input_ = input(user_input)
        user_input = user_input + input_ if input_[-1] != "#" else user_input + input_[:-1]
        s = Search(user_input)
        res = s.get_best_k_completions(5)
        print_result(res)
        if input_[-1] == '#':
            user_input = ''


if __name__ == '__main__':
    auto_complete()

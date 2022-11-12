#Minha Kim
#81343818


import p4mechanics
from p4mechanics import GameOver


def print_board(board: p4mechanics.Board) -> None:
    """
    Prints the board given a Board class.
    """
    for row in range(board.rows()):
        board_string = '|'
        for col in range(board.columns()):
            if board.list()[col][row] == ' ':
                board_string += f"   "
            elif "F" in board.list()[col][row]:
                board_string += f"[{board.list()[col][row].replace('F','')}]"
            elif "P" in board.list()[col][row]:
                board_string += f"|{board.list()[col][row].replace('P','')}|"
            elif "*" in board.list()[col][row]:
                board_string += f"*{board.list()[col][row].replace('*','')}*"
            else:
                board_string += f" {board.list()[col][row]} "
        board_string.rstrip()
        board_string += '|'
        print(board_string)
    print(f" {board.columns() * '---'} ")


def print_contents(game_board) -> None:
    """
    Prints the board when "CONTENTS" is used.
    """
    content_string_list = []
    for r in range(game_board.rows()):
        content_string = str(input())
        if len(content_string) != game_board.columns():
            raise ValueError
        content_string_list.append(content_string)
    for row_count in range(game_board.rows()):
        game_board.make_content_list(content_string_list[row_count], row_count)
    game_board.shift_all_down()


def check_for_verts(game_list: list) -> bool:
    """
    Checks for vertical lines (|x|) in the Board. True if found.
    """
    for item in game_list:
        if "P" in str(item):
            return True
    else:
        return False

def check_for_fallers(game_list: list) -> bool:
    """
    Checks for fallers ([x]) in the board. True if found.
    """
    for item in game_list:
        if "F" in str(item):
            return True
    else:
        return False


def check_for_stars(game_list: list) -> bool:
    """
    Checks for matches (*x*) in the board. True if found.
    """
    for sublist in game_list:
        for char in sublist:
            if "*" in str(char):
                return True
    else:
        return False


def input_F(next_input: str, game_board: p4mechanics.Board) -> None:
    """
    Computes move for when F is the first character (creates Faller). 
    """
    game_board.create_faller(next_input)
    print_board(game_board)


def input_blank(game_board: p4mechanics.Board) -> None:
    """
    Computes moves for when the input is blank ("").
    """
    if check_for_stars(game_board.list()):
        game_board.remove_stars()
        game_board.shift_all_down()
        print_board(game_board)
    try:
        vert_bool = check_for_verts(game_board.list()[int(game_board.get_current_col()) - 1])
        if vert_bool:
            raise ValueError
        game_board.gravity(game_board.get_current_col(), game_board.get_top(), 
        game_board.get_mid(), game_board.get_bot(), game_board.get_iter())
        print_board(game_board)
    except GameOver:
        print_board(game_board)
        raise GameOver
    except:
        vert_bool = check_for_verts(game_board.list()[int(game_board.get_current_col()) - 1])
        if vert_bool:
            game_board.get_rid_of_vert_bars()
            game_board.update_match()
        else:
            game_board.all_falls_down()
        print_board(game_board)


def input_R(game_board: p4mechanics.Board) -> None:
    """
    Computes move for when R is used (rotation).
    """
    game_board.rotate_faller()
    print_board(game_board)


def input_LEFT(game_board: p4mechanics.Board) -> None:
    """
    Computes move for when "<" is used (shift left).
    """
    game_board.shift_left_or_right(0)
    print_board(game_board)


def input_RIGHT(game_board: p4mechanics.Board) -> None:
    """
    Computes move for when ">" is used (shift right).
    """
    game_board.shift_left_or_right(1)
    print_board(game_board)


def run() -> None:
    """
    Runs the program.
    """
    row_input = input()
    try:
        if row_input == "Q":
            raise ValueError
        col_input = input()
        if col_input == "Q":
            raise ValueError
        start_state = input()
        if start_state == "Q":
            raise ValueError
        game_board = p4mechanics.Board(int(row_input), int(col_input))
        if start_state == "EMPTY":
            pass
        elif start_state == "CONTENTS":
            print_contents(game_board)
            game_board.update_match()
        else:
            raise ValueError
        print_board(game_board)
        while True:
            next_input = str(input())
            try:
                if next_input == "Q":
                    break
                elif next_input.startswith('F'):
                    input_F(next_input, game_board)
                elif next_input.strip() == "":
                    input_blank(game_board)
                elif next_input == "R":
                    game_board.rotate_faller()
                    print_board(game_board)
                elif next_input == "<":
                    game_board.shift_left_or_right(0)
                    print_board(game_board)
                elif next_input == ">":
                    game_board.shift_left_or_right(1)
                    print_board(game_board)
            except GameOver:
                print("GAME OVER")
                break
            except AttributeError:
                pass
    except ValueError:
        pass


if __name__ == "__main__":
    run()

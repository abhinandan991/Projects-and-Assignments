from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
#representing A's statement as a sentence
A=And(AKnight,AKnave)
knowledge0 = And(
    #A is a Knight if and only if the logical sentence said by A is true, else A is a Knave
    Biconditional(AKnight,A), Biconditional(AKnave,Not(A)),
    Implication(AKnight,Not(AKnave)),
    Implication(AKnave,Not(AKnight))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
#representing A's statement as a sentence
A=And(AKnight,AKnave)
knowledge1 = And(
    #laying down conditions of the game
    Biconditional(AKnight,A), Biconditional(AKnave,Not(A)),
    Biconditional(BKnight,AKnave), Biconditional(BKnave,AKnight),
    Implication(AKnight,Not(AKnave)),
    Implication(AKnave,Not(AKnight))
    
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
#representing A's statement as a sentence
#representing B's statement as a sentence
A=Or(And(AKnight,BKnight),And(AKnave,BKnave))
B=Or(And(AKnight,BKnave),And(AKnave,BKnight))
knowledge2 = And(
    #layig down conditions of the game
    Biconditional(AKnight,A), Biconditional(AKnave,Not(A)),
    Biconditional(BKnight,B), Biconditional(BKnave,Not(B)),
    Implication(AKnight,Not(AKnave)),
    Implication(AKnave,Not(AKnight)),
    Implication(BKnight,Not(BKnave)),
    Implication(BKnave,Not(BKnight))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
#Representing all sentences said by A,B,C as logical sentences
A=And(Or(AKnight,AKnave))
B=And(AKnave)
B=And(CKnave)
C=And(AKnight)
knowledge3 = And(
    #laying down conditions of the game
    Biconditional(AKnight,A), Biconditional(AKnave,Not(A)),
    Biconditional(BKnight,B), Biconditional(BKnave,Not(B)),
    Biconditional(CKnight,C), Biconditional(CKnave,Not(C)),
    Implication(AKnight,Not(AKnave)),
    Implication(AKnave,Not(AKnight)),
    Implication(BKnight,Not(BKnave)),
    Implication(BKnave,Not(BKnight)),
    Implication(CKnight,Not(CKnave)),
    Implication(CKnave,Not(CKnight)),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()

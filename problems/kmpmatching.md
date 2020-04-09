A linear time algorithm that solves the string matching problem
by preprocessing P in O(m) time.
- main idea is to skip some comparisons by using the previous comparison results

Uses an auxiliary array π that is defined as the following:
- π[i] is the largest integer smaller than i such that P[1]...P[π[i]] 
is a suffix of P[1]...P[i]

i       1   2   3   4   5   6   7   8   9   10
Pi      a   b   a   b   a   b   a   b   c   a
π[i]    0   0   1   2   3   4   5   6   0   1

Let's see why this is useful

T =     ABC ABCDAB ABCDABCDABDE
P =     ABCDABD
π =    0000120
π[0] = -1

Start matching at the first position of T:

12345678901234567890123
ABC ABCDAB ABCDABCDABDE
ABCDABD
1234567

Mismatch at 4th letter of P!
We matched k = 3 letters so far, and π[k] = 0
- Thus, there is no point in starting the comparision at T[2], T[3]
Shift P by k - π[k] = 3 - 0 = 3 letters

12345678901234567890123
ABC ABCDAB ABCDABCDABDE
   ABCDABD
   0000120
   1234567

Mismatch at T[4] again!
We matched k = 0 letter this time.
Shift P by k - π[k] = 0 - (-1) = 0 letter (π[0] = -1 by definition)

12345678901234567890123
ABC ABCDAB ABCDABCDABDE
    ABCDABD
    1234567

Mismatch at T[11]!
π[6] = 2 means P[1]P[2] is a suffix of P[1]...P[6]
Shift P by k - π[k] = 6 - 2 = 4 letters

12345678901234567890123
ABC ABCDAB ABCDABCDABDE
        ABCDABD
        0000120
        1234567
    
Again, no point in shifting P by 1, 2, or 3 letters

Mismatch at T[11] again!
Currently 2 letters are matched.
Shift by k - π[k] = 2 - 0 = 2 letters

12345678901234567890123
ABC ABCDAB ABCDABCDABDE
          ABCDABD
          0000120
          1234567

Mistmatch at T[11] again!
Currently no letters are matched
Shift by k - π[k] = 0 - (-1) = 1 letter

12345678901234567890123
ABC ABCDAB ABCDABCDABDE
           ABCDABD
           0000120
           1234567

Mismatch at T[18].
Currently 6 letters are matched.
Shift P by 6 - π[6] = 4 letters

12345678901234567890123
ABC ABCDAB ABCDABCDABDE
               ABCDABD
               0000120
               1234567

Finally, there it is!
Currently 7 letters are matched.
After recording this match (at T[16]...T[22], we shift P again in order to find other matches)
Shift by 7 - π[7] = 7 letters


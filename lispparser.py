import sys

from typing import Any, List

# Parse input string into a list of all parentheses and atoms (int or str),
# exclude whitespaces.
def normalize_str(string: str) -> List[str]:
   str_norm = []
   last_c = None
   for c in string:
      if c.isalnum():
         if last_c.isalnum():
               str_norm[-1] += c
         else:
               str_norm.append(c)
      elif not c.isspace():
         str_norm.append(c)
      last_c = c
   return str_norm

def print_subtree(tree, gap=0) : 

   while True : 

      for node in tree:

         if type(node) == list: 
            print(len(node))
            print_subtree(node)
         else : 
            print(node)
            return


# Generate abstract syntax tree from normalized input.
def get_ast(input_norm: List[str]) -> List[Any]:
   ast = []
   # Go through each element in the input:
   # - if it is an open parenthesis, find matching parenthesis and make recursive
   #   call for content in-between. Add the result as an element to the current list.
   # - if it is an atom, just add it to the current list.
   i = 0
   while i < len(input_norm):
      symbol = input_norm[i]
      if symbol == '(':
         list_content = []
         match_ctr = 1 # If 0, parenthesis has been matched.
         while match_ctr != 0:
               i += 1
               if i >= len(input_norm):
                  raise ValueError("Invalid input: Unmatched open parenthesis.")
               symbol = input_norm[i]
               if symbol == '(':
                  match_ctr += 1
               elif symbol == ')':
                  match_ctr -= 1
               if match_ctr != 0:
                  list_content.append(symbol)             
         ast.append(get_ast(list_content))
      elif symbol == ')':
               raise ValueError("Invalid input: Unmatched close parenthesis.")
      else:
         try:
               ast.append(int(symbol))
         except ValueError:
               ast.append(symbol)
      i += 1
   return ast

def main():
   input_str = '''
   ( Root (span 1 112) (prom 3 45 99 110 112)
( Nucleus (span 1 109) (rel2par Topic-Shift) (prom 3 45 99)
   ( Nucleus (span 1 42) (rel2par Topic-Drift) (prom 3)
      ( Nucleus (span 1 35) (rel2par span) (prom 3)
         ( Nucleus (span 1 9) (rel2par span) (prom 3)
            ( Nucleus (span 1 5) (rel2par span) (prom 3)
               ( Nucleus (span 1 3) (rel2par span) (prom 3)
                  ( Nucleus (span 2 3) (rel2par span) (prom 3)
                  ( Satellite (leaf 1) (rel2par concession) (prom 1) (text  Although bullish dollar sentiment has fizzled, ) )
                     ( Nucleus (leaf 3) (rel2par span) (prom 3) (text a massive sell-off probably won't occur in the near future.) )
                     ( Satellite (leaf 2) (rel2par attribution) (prom 2) (text many currency analysts say ) )
                  )
               ( Satellite (span 4 5) (rel2par explanation-argumentative) (prom 5)
                  ( Nucleus (leaf 5) (rel2par span) (prom 5) (text weakness in the pound and the yen is expected to offset those factors.) )
                  ( Satellite (leaf 4) (rel2par antithesis) (prom 4) (text  While Wall Street's tough times and lower U.S. interest rates continue to undermine the dollar, ) )
               )
               )
            ( Satellite (span 6 9) (rel2par interpretation-s) (prom 6)
               ( Nucleus (span 6 7) (rel2par span) (prom 6)
                  ( Nucleus (leaf 6) (rel2par span) (prom 6) (text  By default, the dollar probably will be able to hold up pretty well in coming days,) )
                  ( Satellite (leaf 7) (rel2par attribution) (prom 7) (text  says Francoise Soares-Kemp, a foreign-exchange adviser at Credit Suisse.) )
               ( Satellite (span 8 9) (rel2par elaboration-additional) (prom 8)
                  ( Nucleus (leaf 8) (rel2par span) (prom 8) (text  We're close to the bottom of the near-term ranges, ) )
                  ( Satellite (leaf 9) (rel2par attribution) (prom 9) (text she contends.) )
               )
               )
            )
            )
         ( Satellite (span 10 35) (rel2par elaboration-additional) (prom 10 11 12)
            ( Nucleus (span 10 24) (rel2par span) (prom 10 11 12)
               ( Nucleus (span 10 12) (rel2par span) (prom 10 11 12)
                  ( Nucleus (span 10 11) (rel2par Sequence) (prom 10 11)
                     ( Nucleus (leaf 10) (rel2par Contrast) (prom 10) (text  In late Friday afternoon New York trading, the dollar was at 1.8300 marks and 141.65 yen, off from late Thursday's 1.8400 marks and 142.10 yen.) )
                     ( Nucleus (leaf 11) (rel2par Contrast) (prom 11) (text  The pound strengthened to $1.5795 from $1.5765.) )
                  )
                  ( Nucleus (leaf 12) (rel2par Sequence) (prom 12) (text  In Tokyo Monday, the U.S. currency opened for trading at 141.70 yen, down from Friday's Tokyo close of 142.75 yen.) )
               ( Satellite (span 13 24) (rel2par background) (prom 13 19 21 23)
                  ( Nucleus (span 13 18) (rel2par Contrast) (prom 13)
                     ( Nucleus (span 13 16) (rel2par span) (prom 13)
                        ( Nucleus (span 13 16) (rel2par span) (prom 13)
                           ( Nucleus (leaf 13) (rel2par span) (prom 13) (text  The dollar began Friday on a firm note, ) )
                           ( Satellite (span 14 16) (rel2par manner) (prom 14)
                              ( Nucleus (leaf 14) (rel2par span) (prom 14) (text gaining against all major currencies in Tokyo dealings and early European trading ) )
                              ( Satellite (span 15 16) (rel2par concession) (prom 15)
                                 ( Nucleus (leaf 15) (rel2par span) (prom 15) (text despite reports ) )
                                 ( Satellite (leaf 16) (rel2par elaboration-object-attribute-e) (prom 16) (text that the Bank of Japan was seen unloading dollars around 142.70 yen.) )
                              )
                           )
                        )
                     ( Satellite (span 17 18) (rel2par explanation-argumentative) (prom 17)
                        ( Nucleus (leaf 17) (rel2par span) (prom 17) (text  The rise came ) )
                        ( Satellite (leaf 18) (rel2par circumstance) (prom 18) (text as traders continued to dump the pound after the sudden resignation Thursday of British Chancellor of the Exchequer Nigel Lawson.) )
                     )
                     )
                  )
                  ( Nucleus (span 19 24) (rel2par Contrast) (prom 19 21 23)
                     ( Nucleus (span 19 22) (rel2par Same-Unit) (prom 19 21)
                        ( Nucleus (span 19 21) (rel2par span) (prom 19 21)
                           ( Nucleus (leaf 19) (rel2par Same-Unit) (prom 19) (text  But ) )
                           ( Nucleus (span 20 21) (rel2par Same-Unit) (prom 21)
                              ( Nucleus (leaf 21) (rel2par span) (prom 21) (text the dollar was dragged down, ) )
                              ( Satellite (leaf 20) (rel2par circumstance-e) (prom 20) (text once the pound steadied with help from purchases by the Bank of England and the Federal Reserve Bank of New York, ) )
                           )
                        ( Satellite (leaf 22) (rel2par attribution-e) (prom 22) (text traders say, ) )
                        )
                     )
                     ( Nucleus (span 23 24) (rel2par Same-Unit) (prom 23)
                        ( Nucleus (leaf 23) (rel2par span) (prom 23) (text by the stock-market slump ) )
                        ( Satellite (leaf 24) (rel2par elaboration-object-attribute-e) (prom 24) (text that left the Dow Jones Industrial Average with a loss of 17.01 points.) )
                     )
                  )
               )
               )
            ( Satellite (span 25 35) (rel2par interpretation-s) (prom 29 30)
               ( Nucleus (span 25 29) (rel2par List) (prom 29)
                  ( Nucleus (leaf 29) (rel2par span) (prom 29) (text the dollar is still in a precarious position.) )
                  ( Satellite (span 25 28) (rel2par attribution) (prom 25 28)
                     ( Nucleus (span 25 27) (rel2par Same-Unit) (prom 25)
                        ( Nucleus (leaf 25) (rel2par span) (prom 25) (text  With the stock market wobbly and dollar buyers ) )
                        ( Satellite (span 26 27) (rel2par elaboration-object-attribute-e) (prom 26)
                           ( Nucleus (leaf 26) (rel2par span) (prom 26) (text discouraged by signs of U.S. economic weakness and the recent decline in U.S. interest rates ) )
                           ( Satellite (leaf 27) (rel2par elaboration-object-attribute-e) (prom 27) (text that has diminished the attractiveness of dollar-denominated investments, ) )
                        )
                     )
                     ( Nucleus (leaf 28) (rel2par Same-Unit) (prom 28) (text traders say ) )
                  )
               )
               ( Nucleus (span 30 35) (rel2par List) (prom 30)
                  ( Nucleus (span 30 32) (rel2par span) (prom 30)
                     ( Nucleus (span 30 31) (rel2par span) (prom 30)
                        ( Nucleus (leaf 30) (rel2par span) (prom 30) (text  They'll be looking at levels ) )
                        ( Satellite (leaf 31) (rel2par elaboration-object-attribute-e) (prom 31) (text to sell the dollar, ) )
                     ( Satellite (leaf 32) (rel2par attribution) (prom 32) (text says James Scalfaro, a foreign-exchange marketing representative at Bank of Montreal.) )
                     )
                  ( Satellite (span 33 35) (rel2par elaboration-additional) (prom 35)
                     ( Nucleus (leaf 35) (rel2par span) (prom 35) (text  Mr. Scalfaro and others don't see the currency decisively sliding under support at 1.80 marks and 140 yen soon.) )
                     ( Satellite (span 33 34) (rel2par antithesis) (prom 34)
                        ( Nucleus (leaf 34) (rel2par span) (prom 34) (text the dollar eventually could test support at 1.75 marks and 135 yen,) )
                        ( Satellite (leaf 33) (rel2par attribution) (prom 33) (text  While some analysts say ) )
                     )
                  )
                  )
               )
            )
            )
         )
         )
      ( Satellite (span 36 42) (rel2par interpretation-s) (prom 36)
         ( Nucleus (span 36 38) (rel2par span) (prom 36)
            ( Nucleus (span 36 37) (rel2par span) (prom 36)
               ( Nucleus (leaf 36) (rel2par span) (prom 36) (text  Predictions for limited dollar losses are based largely on the pound's weak state after Mr. Lawson's resignation and the yen's inability ) )
               ( Satellite (leaf 37) (rel2par elaboration-object-attribute-e) (prom 37) (text to strengthen substantially ) )
            ( Satellite (leaf 38) (rel2par circumstance) (prom 38) (text when there are dollar retreats.) )
            )
         ( Satellite (span 39 42) (rel2par elaboration-additional) (prom 40)
            ( Nucleus (span 39 41) (rel2par span) (prom 40)
               ( Nucleus (span 40 41) (rel2par span) (prom 40)
               ( Satellite (leaf 39) (rel2par circumstance) (prom 39) (text  With the pound and the yen lagging behind other major currencies, ) )
                  ( Nucleus (leaf 40) (rel2par span) (prom 40) (text you don't have a confirmation ) )
                  ( Satellite (leaf 41) (rel2par elaboration-object-attribute-e) (prom 41) (text that a sharp dollar downturn is in the works,) )
               )
            ( Satellite (leaf 42) (rel2par attribution) (prom 42) (text  says Mike Malpede, senior currency analyst at Refco Inc. in Chicago.) )
            )
         )
         )
      )
      )
   )
   ( Nucleus (span 43 98) (rel2par Topic-Drift) (prom 45)
      ( Nucleus (span 43 93) (rel2par span) (prom 45)
         ( Nucleus (span 43 61) (rel2par span) (prom 45)
            ( Nucleus (span 43 48) (rel2par span) (prom 45)
               ( Nucleus (span 43 45) (rel2par span) (prom 45)
                  ( Nucleus (span 44 45) (rel2par span) (prom 45)
                  ( Satellite (leaf 43) (rel2par circumstance) (prom 43) (text  As far as the pound goes, ) )
                     ( Nucleus (leaf 45) (rel2par span) (prom 45) (text a slide toward support at $1.5500 may be a favorable development for the dollar this week. ) )
                     ( Satellite (leaf 44) (rel2par attribution) (prom 44) (text some traders say ) )
                  )
               ( Satellite (span 46 48) (rel2par elaboration-additional) (prom 48)
                  ( Nucleus (span 47 48) (rel2par span) (prom 48)
                  ( Satellite (leaf 46) (rel2par concession) (prom 46) (text  While the pound has attempted to stabilize, ) )
                     ( Nucleus (leaf 48) (rel2par span) (prom 48) (text it is in critical condition.) )
                     ( Satellite (leaf 47) (rel2par attribution) (prom 47) (text currency analysts say ) )
                  )
               )
               )
            ( Satellite (span 49 61) (rel2par evidence) (prom 49 50)
               ( Nucleus (span 49 50) (rel2par span) (prom 49 50)
                  ( Nucleus (leaf 49) (rel2par Temporal-Same-Time) (prom 49) (text  Sterling plunged about four cents Thursday ) )
                  ( Nucleus (leaf 50) (rel2par Temporal-Same-Time) (prom 50) (text and hit the week's low of $1.5765 ) )
               ( Satellite (span 51 61) (rel2par circumstance) (prom 51 53)
                  ( Nucleus (span 51 52) (rel2par Sequence) (prom 51)
                     ( Nucleus (leaf 51) (rel2par span) (prom 51) (text when Mr. Lawson resigned from his six-year post ) )
                     ( Satellite (leaf 52) (rel2par reason) (prom 52) (text because of a policy squabble with other cabinet members.) )
                  )
                  ( Nucleus (span 53 61) (rel2par Sequence) (prom 53)
                     ( Nucleus (span 53 59) (rel2par span) (prom 53)
                        ( Nucleus (leaf 53) (rel2par span) (prom 53) (text  He was succeeded by John Major, ) )
                        ( Satellite (span 54 59) (rel2par elaboration-additional-e) (prom 54 55)
                           ( Nucleus (leaf 54) (rel2par Problem-Solution) (prom 54) (text who Friday expressed a desire for a firm pound ) )
                           ( Nucleus (span 55 59) (rel2par Problem-Solution) (prom 55)
                              ( Nucleus (leaf 55) (rel2par span) (prom 55) (text and supported the relatively high British interest rates ) )
                              ( Satellite (span 56 59) (rel2par elaboration-object-attribute-e) (prom 56 58)
                                 ( Nucleus (span 56 57) (rel2par Same-Unit) (prom 56)
                                    ( Nucleus (leaf 56) (rel2par span) (prom 56) (text that ) )
                                    ( Satellite (leaf 57) (rel2par attribution-e) (prom 57) (text he said ) )
                                 )
                                 ( Nucleus (span 58 59) (rel2par Same-Unit) (prom 58)
                                    ( Nucleus (leaf 58) (rel2par span) (prom 58) (text are working exactly as intended ) )
                                    ( Satellite (leaf 59) (rel2par purpose) (prom 59) (text in reducing inflation.) )
                                 )
                              )
                           )
                        )
                     ( Satellite (span 60 61) (rel2par interpretation-s) (prom 60)
                        ( Nucleus (leaf 60) (rel2par span) (prom 60) (text  But the market remains uneasy about Mr. Major's policy strategy and the prospects for the pound, ) )
                        ( Satellite (leaf 61) (rel2par attribution) (prom 61) (text currency analysts contend.) )
                     )
                     )
                  )
               )
               )
            )
            )
         ( Satellite (span 62 93) (rel2par elaboration-additional) (prom 64 66)
            ( Nucleus (span 62 70) (rel2par span) (prom 64 66)
               ( Nucleus (span 62 66) (rel2par span) (prom 64 66)
                  ( Nucleus (span 64 66) (rel2par span) (prom 64 66)
                  ( Satellite (span 62 63) (rel2par concession) (prom 62)
                     ( Nucleus (leaf 62) (rel2par span) (prom 62) (text  Although the Bank of England's tight monetary policy has fueled worries ) )
                     ( Satellite (leaf 63) (rel2par elaboration-object-attribute-e) (prom 63) (text that Britain's slowing economy is headed for a recession, ) )
                  )
                     ( Nucleus (span 64 65) (rel2par Same-Unit) (prom 64)
                        ( Nucleus (leaf 64) (rel2par span) (prom 64) (text it is widely believed that Mr. Lawson's willingness ) )
                        ( Satellite (leaf 65) (rel2par elaboration-object-attribute-e) (prom 65) (text to prop up the pound with interest-rate increases ) )
                     )
                     ( Nucleus (leaf 66) (rel2par Same-Unit) (prom 66) (text helped stem pound selling in recent weeks.) )
                  )
               ( Satellite (span 67 70) (rel2par hypothetical) (prom 70)
                  ( Nucleus (leaf 70) (rel2par span) (prom 70) (text that currency is expected to fall sharply.) )
                  ( Satellite (span 67 69) (rel2par condition) (prom 67)
                     ( Nucleus (leaf 67) (rel2par span) (prom 67) (text  If there are any signs ) )
                     ( Satellite (span 68 69) (rel2par elaboration-object-attribute-e) (prom 68)
                        ( Nucleus (leaf 68) (rel2par span) (prom 68) (text that Mr. Major will be less inclined to use interest-rate boosts ) )
                        ( Satellite (leaf 69) (rel2par purpose) (prom 69) (text to rescue the pound from another plunge, ) )
                     )
                  )
               )
               )
            ( Satellite (span 71 93) (rel2par interpretation-s) (prom 71 81)
               ( Nucleus (span 71 80) (rel2par Contrast) (prom 71)
                  ( Nucleus (span 71 73) (rel2par span) (prom 71)
                     ( Nucleus (span 71 72) (rel2par span) (prom 71)
                        ( Nucleus (leaf 71) (rel2par span) (prom 71) (text  It's fair to say there are more risks for the pound under Major ) )
                        ( Satellite (leaf 72) (rel2par comparison) (prom 72) (text than there were under Lawson, ) )
                     ( Satellite (leaf 73) (rel2par attribution) (prom 73) (text says Malcolm Roberts, a director of international bond market research at Salomon Brothers in London.) )
                     )
                  ( Satellite (span 74 80) (rel2par elaboration-additional) (prom 77)
                     ( Nucleus (span 76 80) (rel2par span) (prom 77)
                     ( Satellite (span 74 75) (rel2par antithesis) (prom 74)
                        ( Nucleus (leaf 74) (rel2par span) (prom 74) (text  There's very little upside to sterling, ) )
                        ( Satellite (leaf 75) (rel2par attribution) (prom 75) (text Mr. Roberts says, ) )
                     )
                        ( Nucleus (span 77 80) (rel2par span) (prom 77)
                        ( Satellite (leaf 76) (rel2par attribution) (prom 76) (text but he adds ) )
                           ( Nucleus (leaf 77) (rel2par span) (prom 77) (text that near-term losses may be small) )
                           ( Satellite (span 78 80) (rel2par consequence-n) (prom 78 80)
                              ( Nucleus (span 78 79) (rel2par Same-Unit) (prom 78)
                                 ( Nucleus (leaf 78) (rel2par span) (prom 78) (text  because the selling wave ) )
                                 ( Satellite (leaf 79) (rel2par elaboration-object-attribute-e) (prom 79) (text that followed Mr. Major's appointment ) )
                              )
                              ( Nucleus (leaf 80) (rel2par Same-Unit) (prom 80) (text apparently has run its course.) )
                           )
                        )
                     )
                  )
                  )
               )
               ( Nucleus (span 81 93) (rel2par Contrast) (prom 81)
                  ( Nucleus (span 81 83) (rel2par span) (prom 81)
                     ( Nucleus (leaf 81) (rel2par span) (prom 81) (text  But some other analysts have a stormier forecast for the pound, ) )
                     ( Satellite (span 82 83) (rel2par reason) (prom 82 83)
                        ( Nucleus (leaf 82) (rel2par List) (prom 82) (text particularly because Britain's inflation is hovering at a relatively lofty annual rate of about 7.6% ) )
                        ( Nucleus (leaf 83) (rel2par List) (prom 83) (text and the nation is burdened with a struggling government and large current account and trade deficits.) )
                     )
                  ( Satellite (span 84 93) (rel2par example) (prom 84)
                     ( Nucleus (span 84 86) (rel2par span) (prom 84)
                        ( Nucleus (span 84 85) (rel2par span) (prom 84)
                           ( Nucleus (leaf 84) (rel2par span) (prom 84) (text  The pound likely will fall in coming days ) )
                           ( Satellite (leaf 85) (rel2par elaboration-additional) (prom 85) (text and may trade as low as 2.60 marks within the next year, ) )
                        ( Satellite (leaf 86) (rel2par attribution) (prom 86) (text says Nigel Rendell, an international economist at James Capel & Co. in London.) )
                        )
                     ( Satellite (span 87 93) (rel2par elaboration-additional) (prom 87)
                        ( Nucleus (leaf 87) (rel2par span) (prom 87) (text  The pound was at 2.8896 marks late Friday, off sharply from 2.9511 in New York trading a week earlier.) )
                        ( Satellite (span 88 93) (rel2par interpretation-s) (prom 89)
                           ( Nucleus (span 88 90) (rel2par span) (prom 89)
                              ( Nucleus (span 88 89) (rel2par span) (prom 89)
                                 ( Nucleus (leaf 89) (rel2par span) (prom 89) (text the Bank of England may raise Britain's base lending rate by one percentage point to 16%, ) )
                                 ( Satellite (leaf 88) (rel2par condition) (prom 88) (text  If the pound falls closer to 2.80 marks, ) )
                              ( Satellite (leaf 90) (rel2par attribution) (prom 90) (text says Mr. Rendell.) )
                              )
                           ( Satellite (span 91 93) (rel2par antithesis) (prom 91 93)
                              ( Nucleus (span 91 92) (rel2par Same-Unit) (prom 91)
                                 ( Nucleus (leaf 91) (rel2par span) (prom 91) (text  But such an increase,) )
                                 ( Satellite (leaf 92) (rel2par attribution-e) (prom 92) (text  he says, ) )
                              )
                              ( Nucleus (leaf 93) (rel2par Same-Unit) (prom 93) (text could be viewed by the market as too little too late.) )
                           )
                           )
                        )
                     )
                     )
                  )
                  )
               )
            )
            )
         )
         )
      ( Satellite (span 94 98) (rel2par problem-solution-s) (prom 94)
         ( Nucleus (span 94 97) (rel2par span) (prom 94)
            ( Nucleus (span 94 95) (rel2par span) (prom 94)
               ( Nucleus (leaf 94) (rel2par span) (prom 94) (text  The Bank of England indicated its desire ) )
               ( Satellite (leaf 95) (rel2par elaboration-object-attribute-e) (prom 95) (text to leave its monetary policy unchanged Friday ) )
            ( Satellite (span 96 97) (rel2par manner) (prom 96)
               ( Nucleus (leaf 96) (rel2par span) (prom 96) (text by declining to raise the official 15% discount-borrowing rate ) )
               ( Satellite (leaf 97) (rel2par elaboration-object-attribute-e) (prom 97) (text that it charges discount houses, ) )
            )
            )
         ( Satellite (leaf 98) (rel2par attribution) (prom 98) (text analysts say.) )
         )
      )
      )
   )
   ( Nucleus (span 99 109) (rel2par Topic-Drift) (prom 99)
      ( Nucleus (span 99 100) (rel2par span) (prom 99)
         ( Nucleus (leaf 99) (rel2par span) (prom 99) (text  Pound concerns aside, the lack of strong buying interest in the yen is another boon for the dollar, ) )
         ( Satellite (leaf 100) (rel2par attribution) (prom 100) (text many traders say. ) )
      ( Satellite (span 101 109) (rel2par explanation-argumentative) (prom 101)
         ( Nucleus (span 101 103) (rel2par span) (prom 101)
            ( Nucleus (span 101 102) (rel2par span) (prom 101)
               ( Nucleus (leaf 101) (rel2par span) (prom 101) (text  The dollar has a natural base of support around 140 yen ) )
               ( Satellite (leaf 102) (rel2par consequence-n) (prom 102) (text because the Japanese currency hasn't been purchased heavily in recent weeks, ) )
            ( Satellite (leaf 103) (rel2par attribution) (prom 103) (text says Ms. Soares-Kemp of Credit Suisse.) )
            )
         ( Satellite (span 104 109) (rel2par interpretation-s) (prom 104 106 109)
            ( Nucleus (span 104 105) (rel2par Same-Unit) (prom 104)
               ( Nucleus (leaf 104) (rel2par span) (prom 104) (text  The yen's softness,) )
               ( Satellite (leaf 105) (rel2par attribution-e) (prom 105) (text  she says, ) )
            )
            ( Nucleus (span 106 108) (rel2par Same-Unit) (prom 106)
               ( Nucleus (leaf 106) (rel2par span) (prom 106) (text apparently stems from Japanese investors' interest ) )
               ( Satellite (span 107 108) (rel2par elaboration-object-attribute-e) (prom 107)
                  ( Nucleus (leaf 107) (rel2par span) (prom 107) (text in buying dollars against the yen ) )
                  ( Satellite (leaf 108) (rel2par purpose) (prom 108) (text to purchase U.S. bond issues ) )
               )
            )
            ( Nucleus (leaf 109) (rel2par Same-Unit) (prom 109) (text and persistent worries about this year's upheaval in the Japanese government.) )
         )
         )
      )
      )
   )
)
( Nucleus (span 110 112) (rel2par Topic-Shift) (prom 110 112)
   ( Nucleus (span 110 111) (rel2par Sequence) (prom 110)
      ( Nucleus (leaf 110) (rel2par span) (prom 110) (text  On New York's Commodity Exchange Friday, gold for current delivery jumped $5.80, to $378.30 an ounce, the highest settlement since July 12.) )
      ( Satellite (leaf 111) (rel2par evaluation-s) (prom 111) (text  Estimated volume was a heavy seven million ounces.) )
   )
   ( Nucleus (leaf 112) (rel2par Sequence) (prom 112) (text  In early trading in Hong Kong Monday, gold was quoted at $378.87 an ounce.) )
)
)


   '''
   input_norm = normalize_str(input_str)
   ast = get_ast(input_norm)
   
   # for i in range(len(ast)) : 

   #    print('t'*i , ast[i])

   parsed = []
      
   tree = ast[0]

   print(len(ast))

   for node in ast : 



      if node[0] in ['Root', 'Nucleus', 'Satellite']: 

         print(node[0] , ' encountered')


   

   def ptree(ast, tab_count = 0) : 

      
      stack = []

      for node in ast : 

         if node[0] in ['Root'] : 
            
            print(tab_count, tab_count*' ', node[0])
            ptree(node, tab_count = tab_count+1)

         elif node[0] in [ 'Nucleus'] : 
            tab_count += 1
            print(tab_count, tab_count*' ', node[0])
            ptree(node, tab_count = tab_count+1)

         elif node[0] in ['Satellite'] : 
            print(tab_count, tab_count*' ', node[0])
            ptree(node, tab_count = tab_count-1)
            
            
         # else : 

         #    print(tab_count*'\t', node[0])

   ptree(ast)


    

if __name__ == '__main__':
   main()
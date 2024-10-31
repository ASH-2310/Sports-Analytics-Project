# Sports-Analytics-Project
### About Moneyball
Moneyball is a renowned real-world example of sports analytics. The Oakland Athletics, a small-market team, used data-driven strategies to compete with big-market teams despite limited resources. Billy Beane and Paul DePodesta, leveraging statistical analysis, identified undervalued players and exploited market inefficiencies. By prioritizing advanced metrics like on-base percentage over traditional scouting methods, they built a competitive team on a tight budget. Their unconventional approach challenged baseball's conventional wisdom and proved that data-driven decision-making can level the playing field in professional sports.
### Paul Depodesta’s Model
According to DePodesta, A’s required at least 99 wins in order to make the playoffs in 2002. DePodesta also calculated that the A’s need to score at least 814 runs and allow only 645 runs in order to make it to the postseason. 
### My Approach
I filtered the Dataset and considered only those teams who got into the playoffs, to drive an accurate winning formula. 
Moneyball = pd.read_csv(r"C:\Users\LENOVO\Downloads\baseball.csv")
Moneyball_new = Moneyball[(Moneyball['Playoffs'] == 1)]
### My Model
Based on my analysis, it has been determined that in order to secure a spot in the playoffs, a team must win at least 103 games while also achieving a minimum of 827 runs scored. These criteria have been identified as crucial benchmarks for playoff qualification. Our regression equation is as follows:
RS = -722.67371525 + 2509.17078846(OBP) + 1608.371836 (SLG)  - 18.95402629(BA)
In the below equation I have removed batting average because a negative impact of batting average on runs scored do not make any sense. The new equation is as follows:
RS = -724.10767069 + 2501.62875546 (OBP) + 1605.76633709 (SLG)
Substituting values for year 2001
RS = -724.10767069 + 2501.62875546 (0.345) + 1605.76633709 (0.429)
RS = 827
I also wanted to see how many Runs  allowed to get the team into playoffs. Regression equation of opponents is as follows:
RA = -150.62956757 + 3562.03594647 (OOBP) - 899.90448567 (OSLG)
Substituting values for year 2001
RA = -150.62956757 + 3562.03594647 (0.308) - 899.90448567 (0.38)
RA = 604
## WINNING FORMULA 
### Linear Regression Results
Based on my analysis, I came to the conclusion that 604 Runs should be allowed and Run difference should be of 223 at minimal for Oakland Athletics' to get into playoffs. 
**Runs Scored = 827 
Runs Allowed = 604
Runs Difference = 827 – 604 = 223
Wins = 85.60 + 0.0798(223)
Wins = 103**
### Logistic Regression Results
According to my model, teams with atleast 103 wins have 97% chances of getting in the playoffs.









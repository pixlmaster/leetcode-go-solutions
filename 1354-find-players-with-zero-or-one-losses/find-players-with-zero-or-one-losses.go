func findWinners(matches [][]int) [][]int {
    // players vs number of losses map
    lossCount := make(map[int]int)
    for _, match := range matches {
        winner := match[0]
        loser := match[1]
        _, winnerFound := lossCount[winner]
        _, loserFound := lossCount[loser]
        // winner has not lost any matches yet
        if !winnerFound {
            lossCount[winner] = 0
        }
        // 1st loss of the player
        if !loserFound {
            lossCount[loser] = 1
        } else {
            // 1st loss after all wins OR another loss
            lossCount[loser]++
        }
    }

    var losers0 []int
    var losers1 []int
    for player, losses := range lossCount{
        if losses == 0 {
            losers0 = append(losers0, player)
        } else if losses ==1 {
            losers1 = append(losers1, player)
        }
    }
    sort.Ints(losers0)
    sort.Ints(losers1)

    var ans [][]int
    ans = append(ans, losers0)
    ans = append(ans, losers1)
    return ans
}
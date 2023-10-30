func isValid(s string) bool {
    open_count := 0
    for i, c := range s {
        if c == '(' {
            open_count += 1
        } else {
            if open_count > 0 {
                open_count -= 1
                } else {
                return false
                }
        }
    return open_count == 0
    }
}


func longestValidParentheses(s string) int {

}
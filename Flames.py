from collections import Counter

def main_gmae():
    print("Flames Checker, by B.P.X")
    name1 = input("Enter First Name: ")
    name2 = input("Enter Second Name: ")

    flames_dict = {
        "F" : "Friends",
        "L" : "Love",
        "A" : "Affection",
        "M" : "Marriage",
        "E" : "Enemies",
        "S" : "Siblings"
    }

    def check_names(name3, name4):
        n1 = [char for char in name3.upper() if not char.isspace()]
        n2 = [char for char in name4.upper() if not char.isspace()]
        cnt1 = Counter(n1)
        cnt2 = Counter(n2)

        # Remove common characters
        for char in list(cnt1.keys()):
            if char in cnt2:
                common = min(cnt1[char], cnt2[char])
                cnt1[char] -= common
                cnt2[char] -= common

        # Total remaining unmatched characters
        total_unmatched = sum(cnt1.values()) + sum(cnt2.values())
        return total_unmatched

    def flame_check(count1):
        flames = ["F", "L", "A", "M", "E", "S"]
        while len(flames) > 1:
            index = (count1 % len(flames)) - 1
            if index == -1:
                index = len(flames) - 1
            flames.pop(index)
            flames = flames[index:] + flames[:index]
        result = flames[0]
        return result
    count = check_names(name1, name2)
    res = flame_check(count)
    print(f"Your Relationship status is : {flames_dict[res]}!")

main_gmae()
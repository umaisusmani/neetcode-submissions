class Solution {
    isAnagram(s: string, t: string): boolean {
        if (s.length === t.length)
        {
            let SChar = new Map<string, number>();
            let TChar = new Map<string, number>();

            for (let n = 0; n < s.length; n++)
            {
                SChar.set(s[n], (SChar.get(s[n]) || 0) + 1);
                TChar.set(t[n], (TChar.get(t[n]) || 0) + 1);
            }
            for (const j of SChar.keys())
            {
                if (!(SChar.get(j) === TChar.get(j)))
                {
                    return false;
                }
            }
            return true;
        }
        else
        {
            return false;
        }
    }
}
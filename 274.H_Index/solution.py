class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        h = 0

        for citation in citations:
            if citation >= h + 1:
                h += 1
            else:
                break
        
        return h
        
    '''
    Sort array first

    6 5 3 1 0

    h initialized at 0

    6: h can be 1 
    5: h can be 2 
    3: h can be 3
    1: h can't be 4 
    return h = 3
    '''
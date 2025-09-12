def merge_sorted_lists( l1 , l2 ) :
    new = Node()



def serie( head ) :
    if head is None :
        return None
    curr = head
    while curr.next is not None :
        if curr.val <= curr.enxt.val :
            curr = curr.next
        else :
            second = curr.next
            curr.next=None
            curr_2 = second
            while curr_2.enxt is not None  :
                if curr_2.val <= curr.next.val :
                    curr_2 =curr_2.next
                else :
                    temp = curr_2
                    curr_2 = curr_2.next
                    temp.next = None

            if curr_2.next is None :
                curr_2 = None
            if curr.next is None :
                second = None
            return head , second , curr_2

#end serie

def merge_sort( head) :
    curr = head
    while True :
        first , second , third = serie( curr )

        while second is not None and third is not None :
            if second is None:
                break
            beg , end = merge_sorted_lists( first , second )
            end.next = third
            first, second, third = serie( third )
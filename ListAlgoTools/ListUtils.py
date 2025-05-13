class ListUtils:

    @staticmethod
    def insert_sorted(lst, value):
        if lst is None:
            return
        if lst=="" and value!=0:
            lst.append(value)
        index=len(lst)
        lst.append(0)
        i=len(lst)-2
        while i>=0 and lst[i]>value:
            lst[i+1]=lst[i]
            i-=1
        lst[i+1]=value
        """
        Inserts value into the list so that it remains sorted (ascending order).
        Assumes list is already sorted.
        """

    @staticmethod
    def remove_maximum_values(lst, N):
        if lst==None or N<=0:
            return
        sorted_arr=[]
        lst_copy=lst.copy()
        for i in lst:
            sorted_arr.append(i)
        for i in range(len(sorted_arr)):
            for j in range(i+1, len(sorted_arr)):
                if sorted_arr[i]>sorted_arr[j]:
                    temp=sorted_arr[i]
                    sorted_arr[i]=sorted_arr[j]
                    sorted_arr[j]=temp
        max_values=[]
        i=len(sorted_arr)-1
        while i>=0 and len(max_values)<N:
            if sorted_arr[i] not in max_values:
                max_values.append(sorted_arr[i])
            i -= 1
        lst.clear()
        for i in lst_copy:
            if i not in max_values:
                lst.append(i)
        """
        Removes the N largest unique values from the list.
        """

    @staticmethod
    def contains_subsequence(one, two):
        if one==None or two==None:
            return False
        if len(one)==0 or len(two)==0:
            return False
        i=0
        while i<=len(one)-len(two):
            j=0
            while j<len(two):
                if one[i+j]!=two[j]:
                    break
                j+=1
            if j==len(two):
                return True
            i+=1
        return False
            
        """
        Returns True if `two` appears as a consecutive subsequence in `one`.
        """
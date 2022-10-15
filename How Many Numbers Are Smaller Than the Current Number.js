
function smallerNumbersThanCurrent(nums) {
    var c=[];
 for(var x=0; x<nums.length; x++){
      c[x]=0

   }
   for(let i=0; i<nums.length;i++)
      
       {
           for(let j=0; j<nums.length;j++)
               {
                 if(nums[i]>nums[j])
                     {
                       c[i]+=1;

                     }
               }
           
            
   }
   return c;

    
};

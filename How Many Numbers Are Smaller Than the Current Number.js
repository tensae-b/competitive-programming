const nums=[8,1,2,2,3];

var c=[0,0,0,0,0];
function smallerNumbersThanCurrent(nums) {
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
    console.log(c);

    
};

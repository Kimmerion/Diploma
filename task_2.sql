-- Скриншот выполнения данного теста называется task2.png.
-- С case все ок, работает. Ничего не меняла, просто отформатировала.
select track,
       case
           when finished then 2
           when cancelled then -1
           when "inDelivery" then 1
           else 0
       end as status
from "Orders";

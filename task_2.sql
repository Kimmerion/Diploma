select track,
case when finished then 2 when cancelled then -1 when "inDelivery" then 1 else 0
 end
from "Orders";
select distinct login
 	from "Couriers"
 	join "Orders" on "Couriers".id = "Orders"."courierId"
where "inDelivery" = true;
from final_project.Recombiner import SimpleRecombiner

testlist=list(range(14))
testlist2=list(range(14))
testlist2.reverse()
parents = []
parents = [({'vehicle_capacities':testlist,'customer_demands':testlist,'capacities_list':[5,2,5,3,2,2,2,4,1,3]},
              {'vehicle_capacities':testlist2,'customer_demands':testlist2,'capacities_list':[5,2,5,3,2,2,2,4,1,3]})]
SR= Simple_Recombiner()
print(SR.recombine(parents))
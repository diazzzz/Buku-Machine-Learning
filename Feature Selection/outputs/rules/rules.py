def findDecision(obj): #obj[0]: Outlook, obj[1]: Temp., obj[2]: Humidity, obj[3]: Wind
	# {"feature": "Outlook", "instances": 14, "metric_value": 0.9403, "depth": 1}
	if obj[0] == 'Sunny':
		# {"feature": "Humidity", "instances": 5, "metric_value": 0.971, "depth": 2}
		if obj[2] == 'High':
			return 'No'
		elif obj[2] == 'Normal':
			return 'Yes'
		else: return 'Yes'
	elif obj[0] == 'Rain':
		# {"feature": "Wind", "instances": 5, "metric_value": 0.971, "depth": 2}
		if obj[3] == 'Weak':
			return 'Yes'
		elif obj[3] == 'Strong':
			return 'No'
		else: return 'No'
	elif obj[0] == 'Overcast':
		return 'Yes'
	else: return 'Yes'

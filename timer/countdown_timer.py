import rx

class CountdownTimer:
	def __init__(self, duration_ms):
		self.duration_ms = duration_ms
		self.remaining_time_ms = duration_ms
		self.observers = set()

	def subscribe(self, observer):
		self.observers.add(observer)

	def start(self):
		self.timer = rx.Observable.timer(1000, 1000);
		self.timer_subscription = self.timer.subscribe(self.__on_tick)

	def __on_tick(self, tick):
		self.remaining_time_ms -= 1000

		# TODO Use Rx
		# TODO Create model for event data
		for observer in self.observers:
			observer.on_tick({
				'remaining_time_ms': self.remaining_time_ms
			})

		if self.remaining_time_ms == 0:
			self.timer_subscription.dispose()
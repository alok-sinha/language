#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <time.h>
#include <unistd.h>



typedef struct {
	int  taskId;
}thread_task_t;


typedef struct {
	thread_task_t *task_queue;
	int max_num_of_tasks;
	int num_of_pending_task;

	pthread_mutex_t lock;
	pthread_cond_t cond;

	int num_of_threads;
	pthread_t *threads;
	void (*func)(void *);
}threadpool_t;

int globalVar = 10;


void *thread_func (void *tpool) {
	threadpool_t *pool = (threadpool_t *)tpool;

	setbuf(stdout, NULL);
	long tid = (long)pthread_self();

	printf("\n Created thread %d(%d)", tid, globalVar);
	globalVar = 20;

	for (;;) {
		pthread_mutex_lock(&pool->lock);

		while (pool->num_of_pending_task <= 0) {
			printf("\n %d : No task yet (%d), waiting for it...", tid, pool->num_of_pending_task);
			pthread_cond_wait(&pool->cond, &pool->lock);
		}

		int i =0;
		while (i < pool->max_num_of_tasks) {
			thread_task_t *task = &pool->task_queue[i];
			printf("\nLooking for available task %d", task->taskId);
			if (task->taskId > 0) {
				printf("\n (%d) Perforning task :  taskid %d", tid, task->taskId);
				
				task->taskId = 0;
				pool->num_of_pending_task -= 1;
				//perform_task();
				break;
			}
			i += 1;
		}
		
		pthread_mutex_unlock(&pool->lock);
	}

	printf("\n$$$$ Done thread %d", tid);
	return NULL;
}

void add_task (int id, threadpool_t *pool) {

	int j = 0;
	
	pthread_mutex_lock(&pool->lock);
	printf("\nAdding tasks : Pending %d, Max %d", pool->num_of_pending_task, pool->max_num_of_tasks);
	while (pool->num_of_pending_task == pool->max_num_of_tasks) {
		pthread_cond_wait(&pool->cond, &pool->lock);
	}
	
	bool signal= false;
	for (j=0; j < pool->max_num_of_tasks; j++) {
		printf("\n%x", pool->task_queue[j]);
		if (pool->task_queue[j].taskId == 0) {
			pool->task_queue[j].taskId = id;
			pool->num_of_pending_task += 1;
			printf("\n Task added : %d(%d)", id, pool->num_of_pending_task);
			signal = true;
			break;
		}
	}

	
	pthread_mutex_unlock(&pool->lock);
	
	if (signal) {
		pthread_cond_broadcast(&pool->cond);
	}
}	



void *master_thread (void *tpool) {
	setbuf(stdout, NULL);

	threadpool_t *pool = (threadpool_t *)tpool;
	for (int i=0; i < 100; i ++) {
		add_task(i+1, pool);
		//sleep(1);
	}
	printf("\nDone adding tasks!!");

	return NULL;
}

threadpool_t *create_thread_pool (int num_of_threads, void *(*tfunc)(void *), int max_num_of_tasks) 
{

	threadpool_t *tpool = (threadpool_t *)malloc(sizeof(threadpool_t));

	if (!tpool) {
		return NULL;
	}
	setbuf(stdout, NULL);

	tpool->max_num_of_tasks = max_num_of_tasks;
	tpool->num_of_pending_task = 0;
	tpool->num_of_threads = num_of_threads;
	pthread_mutex_init(&tpool->lock, NULL);
	pthread_cond_init(&tpool->cond, NULL);
	tpool->task_queue = (thread_task_t *)malloc(sizeof(thread_task_t)*max_num_of_tasks);
	tpool->threads = (pthread_t *)malloc(sizeof(pthread_t)*num_of_threads);

	if (!tpool->task_queue || !tpool->threads) {
		if (tpool->task_queue) {
			free(tpool->task_queue);
		}

		if (tpool->threads) {
			free(tpool->threads);
		}
		free(tpool);
		return NULL;
	}
	memset(tpool->threads, 0, sizeof(pthread_t)*num_of_threads);
	memset(tpool->task_queue, 0, sizeof(thread_task_t)*num_of_threads);

	int count=0;
	for (int i=0; i < num_of_threads; i++) {
		pthread_t tid;
		int ret = pthread_create(&tid, NULL, tfunc, (void *)tpool);
		if (ret == 0) {
			tpool->threads[count] = tid;
			count += 1;
		}
	}
	tpool->num_of_threads = count;

	pthread_t mtid;
	pthread_create(&mtid, NULL, master_thread, (void *)tpool);
	
	for (int i=0; i < tpool->num_of_threads; i++) {
		pthread_join(tpool->threads[i], NULL);
	}
	pthread_join(mtid, NULL);
	printf("\n Done , exiting process!!");


	return (tpool);
}

int main (int argc, char *args[]) {
	create_thread_pool(10, thread_func, 100);
}
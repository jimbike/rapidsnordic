import { defineCollection, z } from 'astro:content';

const post = defineCollection({
  schema: z.object({
    title: z.string(),
    date: z.date(),
    summary: z.string().optional(),
    draft: z.boolean().default(false),
  }),
});

const race = defineCollection({
  schema: z.object({
    title: z.string(),
    date: z.date(),
    location: z.string(),
    venue: z.string(),
    startTime: z.string(),
    format: z.enum(['Skate', 'Classic', 'Pursuit', 'Classic Sprint', 'Skate Sprint', 'Skate and Classic']),
    resultsLink: z.string().optional(),
    registrationLink: z.string().optional(),
    description: z.string().optional(),
    address: z.string().optional(),
    waxRecommendation: z.string().optional(),
    teamGoals: z.array(z.string()).optional(),
    busInfo: z.object({
      departTime: z.string(),
      returnTime: z.string().optional(),
    }).optional(),
    draft: z.boolean().default(false),
  }),
});

export const collections = {
  announcements: post,
  workouts: post,
  races: race,
};
